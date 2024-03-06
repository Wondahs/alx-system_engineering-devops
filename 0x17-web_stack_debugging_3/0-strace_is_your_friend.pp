# Fix Apache Errors

exec { 'replace_phpp_with_php':
  command     => "/usr/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  refreshonly => true,
}
